```json
{
  "id": "2e6cd12b9534bd2c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294309,
  "host_pid": "9e6742732c60:1",
  "hash": "ffbb79923e9cad007fa9b8a8095bf847617557908028b7e7b2346b9b9fa8fc82",
  "cid": "QmV1ffbb79923e9cad007fa9b8a8095bf84761755790",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294309,
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
      "evaluated_at": 1760294309
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
  "sig": "20a2455d7d22cbd8bf4619e921ff3cfe4cec0c2dc8d6dd8b34afa078a124750b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 74788280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}