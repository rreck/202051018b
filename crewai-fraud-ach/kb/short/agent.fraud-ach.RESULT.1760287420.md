```json
{
  "id": "f385553670e7f300",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287420,
  "host_pid": "9e6742732c60:1",
  "hash": "c8b4e7bf8a5e7c9836137a8a422d72038533e0d610ef38326fdfdbfaa02935e4",
  "cid": "QmV1c8b4e7bf8a5e7c9836137a8a422d72038533e0d6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287420,
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
      "evaluated_at": 1760287420
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
  "sig": "98199b562af0a63a0347122fd359a73d602b0b670c637684e9533fd0cec17dc8"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 59, 'threshold': 50, 'total_amount': 18776632, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}