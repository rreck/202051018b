```json
{
  "id": "5781ffd98e162e64",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293305,
  "host_pid": "9e6742732c60:1",
  "hash": "33cbcff05a51a57f183180c519aac62d739b31c37912a60519a766111cd7a706",
  "cid": "QmV133cbcff05a51a57f183180c519aac62d739b31c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293305,
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
      "evaluated_at": 1760293305
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
  "sig": "ed536d36d1cd17b08f7396c1f34de25fce1c25c8b614cdc877a8c428d8f220c7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597374431
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 103085352, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': '588649476db38395'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}