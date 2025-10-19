```json
{
  "id": "cbbfcc3e55b72db5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293132,
  "host_pid": "9e6742732c60:1",
  "hash": "6d5b76fdd905910b1dc0dce681fe9725c181d5de59dce119b276028359865776",
  "cid": "QmV16d5b76fdd905910b1dc0dce681fe9725c181d5de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293132,
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
      "evaluated_at": 1760293132
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
  "sig": "462f42ad6fde9b08b82aa3e949aa4dc18d180ef0521b460703a8ebebbf90a5e7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597950940
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 56480404, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': 'cd3d42208c2780a3'}}}