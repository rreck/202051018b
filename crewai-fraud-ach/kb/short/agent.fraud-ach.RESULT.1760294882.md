```json
{
  "id": "3b0d5762f09dcb25",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294882,
  "host_pid": "9e6742732c60:1",
  "hash": "63aab62766b1d9ae0c4dfde9765cd3619cba7cf7178c235de615205eb34181e5",
  "cid": "QmV163aab62766b1d9ae0c4dfde9765cd3619cba7cf7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294882,
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
      "evaluated_at": 1760294882
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
  "sig": "91bf3d60e721eeb54180b86bef346098a0313c877ff01ce81011edc9158354c5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151773289
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 120998052, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': '7b1e6accdb666d6e'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}