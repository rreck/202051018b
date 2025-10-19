```json
{
  "id": "bc073116c36315c0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290172,
  "host_pid": "9e6742732c60:1",
  "hash": "b1071bcfbfe87350e1044bb1633577c00e68aad11c5dc456d344398ac964a828",
  "cid": "QmV1b1071bcfbfe87350e1044bb1633577c00e68aad1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290172,
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
      "evaluated_at": 1760290172
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
  "sig": "2272c479c014185436629e4412a87e03df97513250f6f89363ca30e45ccfe65d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025325708
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 46082179, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285765, 'matching_hash': '23dd43a9dda0a05d'}}}