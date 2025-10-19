```json
{
  "id": "21134511ce077ef9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293623,
  "host_pid": "9e6742732c60:1",
  "hash": "7886a22c63cac920f939222051018f47f2916625cf66cc9325e486a436cfc573",
  "cid": "QmV17886a22c63cac920f939222051018f47f2916625",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293623,
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
      "evaluated_at": 1760293623
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
  "sig": "96e4bef0d060521717f1dc3fcf6fef0c99f06dc813d14d517e531007c3b58bb2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464924143
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 298, 'threshold': 50, 'total_amount': 121102730, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 297, 'first_seen': 1760284979, 'matching_hash': '7b94effc1b7c4489'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}