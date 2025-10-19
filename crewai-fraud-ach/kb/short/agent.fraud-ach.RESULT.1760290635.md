```json
{
  "id": "e87b920ceef7e42c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290635,
  "host_pid": "9e6742732c60:1",
  "hash": "b4dd55ba62ed9499b1f939a375998e854d517fac80d50aeb0ce274b5f1d4c1bf",
  "cid": "QmV1b4dd55ba62ed9499b1f939a375998e854d517fac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290635,
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
      "evaluated_at": 1760290635
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
  "sig": "606ce881a5deb189fdb3484f3a0def24e22ae95348012d4d2ab0d17b70893850"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247499118
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 11857190, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285765, 'matching_hash': 'f65a723d753f6ade'}}}