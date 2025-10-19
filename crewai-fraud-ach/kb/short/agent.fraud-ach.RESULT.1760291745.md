```json
{
  "id": "facebe499a2feef0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291745,
  "host_pid": "9e6742732c60:1",
  "hash": "4c71100b1bb2b6be26fd9304b4ff7162759a7043894e1dfede68871ef9957320",
  "cid": "QmV14c71100b1bb2b6be26fd9304b4ff7162759a7043",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291745,
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
      "evaluated_at": 1760291745
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
  "sig": "53238cffa638edbc6ce1291bf15f93bd823fd67c7df33c35ca8b5e4b574c645b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596367142
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 82457284, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285763, 'matching_hash': '4f1a5a8d43b99e0b'}}}