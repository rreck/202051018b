```json
{
  "id": "b2730f681f1162d2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290588,
  "host_pid": "9e6742732c60:1",
  "hash": "c235a7c2bd2b55553a5cc5fb726ddcc64a2700721533fbe84a2ca489f83e911d",
  "cid": "QmV1c235a7c2bd2b55553a5cc5fb726ddcc64a270072",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290588,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760290588
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "2f4e5b7120b1b510474422135fec76db09091c329306779a52af9223d38f595e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152729668
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 21597884, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285763, 'matching_hash': 'e33e77be4df2721a'}}}