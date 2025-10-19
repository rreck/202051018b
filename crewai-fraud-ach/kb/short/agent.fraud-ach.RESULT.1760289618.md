```json
{
  "id": "7874d13f7908342a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289618,
  "host_pid": "9e6742732c60:1",
  "hash": "964efdafcfee74e4c152ecb58ae1d87a8d379f8d61dc28cac548e59927645a16",
  "cid": "QmV1964efdafcfee74e4c152ecb58ae1d87a8d379f8d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289618,
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
      "evaluated_at": 1760289618
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
  "sig": "c9a45fab1964524ca1aa8796155ce7733f565a9a2feec99a11e10d58770a2846"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593456245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 61666944, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285764, 'matching_hash': '5bbbd28055422217'}}}