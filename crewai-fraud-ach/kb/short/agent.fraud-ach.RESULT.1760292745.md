```json
{
  "id": "0ecd9d6acef07667",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292745,
  "host_pid": "9e6742732c60:1",
  "hash": "ba34772dd071c9adaaf8dbd6ddfdd1cb97ff15157425bdae72362e7f4e386bcc",
  "cid": "QmV1ba34772dd071c9adaaf8dbd6ddfdd1cb97ff1515",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292745,
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
      "evaluated_at": 1760292745
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
  "sig": "032fa4eba0492165fc83f1d7da2e23852b7880f025104913d3149406aa5f6bb3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153734827
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 100662780, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285764, 'matching_hash': 'f575a9f929aab221'}}}