```json
{
  "id": "0f5aa9c974b71598",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286870,
  "host_pid": "9e6742732c60:1",
  "hash": "19f97f99c27eb99274bf3738e480d9c0031de74775168383e3c828992cc18372",
  "cid": "QmV119f97f99c27eb99274bf3738e480d9c0031de747",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286870,
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
      "evaluated_at": 1760286870
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "0aedc7d7e2eb5d9e6574b834fc36d0bdcdb54d52e09b653fda0f74db91647402"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100278705813
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12589960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760285764, 'matching_hash': '628aaca406e38baa'}}}round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}