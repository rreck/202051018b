```json
{
  "id": "6c00db32c11c43d2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287516,
  "host_pid": "9e6742732c60:1",
  "hash": "cc061ea4dcfa04cda814f57154017889381dcec17c8ae05351b47f47c7add5e0",
  "cid": "QmV1cc061ea4dcfa04cda814f57154017889381dcec1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287516,
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
      "evaluated_at": 1760287516
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
  "sig": "345e6d0125edee9037a77b1dc790ef73fee5da81224bdca1e6ff6e19d827c6c5"
}
```

Fraud detected: duplicate_transaction (score: 80)
Transaction: 044000039326834
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50, 'total_amount': 16134048, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285763, 'matching_hash': '4e66e6716d66a614'}}}