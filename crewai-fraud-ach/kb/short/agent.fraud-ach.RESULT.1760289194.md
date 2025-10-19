```json
{
  "id": "746f5203557a1e1e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289194,
  "host_pid": "9e6742732c60:1",
  "hash": "5d4d693209f9b462c9d4a8f5cb251ef478e5f48f6850203c47224c1f19c5de2e",
  "cid": "QmV15d4d693209f9b462c9d4a8f5cb251ef478e5f48f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289194,
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
      "evaluated_at": 1760289194
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
  "sig": "13bc30afd29f3c02cb92106cecc71f9d0118bdde3eaa89e5441b61f4193391df"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152729668
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 16268536, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285763, 'matching_hash': 'e33e77be4df2721a'}}}