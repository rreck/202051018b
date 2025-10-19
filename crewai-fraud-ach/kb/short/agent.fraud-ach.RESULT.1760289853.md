```json
{
  "id": "ef58409a789d01b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289853,
  "host_pid": "9e6742732c60:1",
  "hash": "a2fa0b0611be79351ef49dbd9cb5bf4c27ceb53252fc2d2459a13862290af3a9",
  "cid": "QmV1a2fa0b0611be79351ef49dbd9cb5bf4c27ceb532",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289853,
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
      "evaluated_at": 1760289853
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
  "sig": "0a8ecf79b9a37e523cf3a9405d396cb5b547467fdce513432e3c4c43d335577a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599039113
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 42635295, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285763, 'matching_hash': 'a57f59a3a9bbca3d'}}}