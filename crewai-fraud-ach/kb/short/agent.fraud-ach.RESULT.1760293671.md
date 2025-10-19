```json
{
  "id": "e4add1d51b869927",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293671,
  "host_pid": "9e6742732c60:1",
  "hash": "3d1a201019ae667064df65c17840883395517a13f23bdcda40a1f5ff00eb8b52",
  "cid": "QmV13d1a201019ae667064df65c17840883395517a13",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293671,
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
      "evaluated_at": 1760293671
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
  "sig": "a669be0526168f8c3f6da34750a22182998e49c9028336f28bf286ea9b8785ae"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030656036
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 299, 'threshold': 50, 'total_amount': 85083739, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 298, 'first_seen': 1760284979, 'matching_hash': '54d3add09935598e'}}}