```json
{
  "id": "49b9580277e453a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288399,
  "host_pid": "9e6742732c60:1",
  "hash": "0876e33e28f2a633456136c8a82b1f31d8e4a6cee48c11c7b9ca2e0432a2ca7f",
  "cid": "QmV10876e33e28f2a633456136c8a82b1f31d8e4a6ce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288399,
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
      "evaluated_at": 1760288399
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
  "sig": "74315b0e23713ee93ff9341ae6dccb18454651f90c24ca269039109a5ede2f6c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024587821
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 39708672, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285765, 'matching_hash': 'e3fd1743fc412dec'}}}}}