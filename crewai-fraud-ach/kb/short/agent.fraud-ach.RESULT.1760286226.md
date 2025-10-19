```json
{
  "id": "0c71cec727010aaa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286226,
  "host_pid": "9e6742732c60:1",
  "hash": "445dafef5d59a2962022d948b19658f64e93044e0bde2618b7397ce58e772f61",
  "cid": "QmV1445dafef5d59a2962022d948b19658f64e93044e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286226,
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
      "evaluated_at": 1760286226
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
  "sig": "a15ca414a3309dd29fe3b86d73a3ba4d8d0625e4d791be5e84d8c59269cf4beb"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105151363741
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285765, 'matching_hash': 'ec824383c23ded7d'}}}