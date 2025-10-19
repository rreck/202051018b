```json
{
  "id": "db864c7dff66f966",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287880,
  "host_pid": "9e6742732c60:1",
  "hash": "966ad43b318df20ba0c46d18dcd8c8ad34de1b7bcf0b4f167fd50129d3dfd793",
  "cid": "QmV1966ad43b318df20ba0c46d18dcd8c8ad34de1b7b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287880,
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
      "evaluated_at": 1760287880
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "8a580c92c61f967c53f1259ba0773d93f579f84529eebdf2764d608f901b5688"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 211815510392855
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50, 'total_amount': 25397175, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285765, 'matching_hash': '64b36e7650337f92'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '211815514', 'validation_error': 'Invalid routing number checksum'}}}