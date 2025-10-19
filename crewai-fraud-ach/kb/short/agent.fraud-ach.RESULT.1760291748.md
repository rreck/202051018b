```json
{
  "id": "b1361939a702537a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291748,
  "host_pid": "9e6742732c60:1",
  "hash": "5f42668b7a671f1afdfad8c998d3eba275c8e7887539d21fe3da802bb1b57c4c",
  "cid": "QmV15f42668b7a671f1afdfad8c998d3eba275c8e788",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291748,
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
      "evaluated_at": 1760291748
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
  "sig": "e0947526798ec50228758b67bc6d1af61d74ba908ae2e20a00355c4943b0c3ab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022625380
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 65827762, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285763, 'matching_hash': 'f6638b44b9180b42'}}}