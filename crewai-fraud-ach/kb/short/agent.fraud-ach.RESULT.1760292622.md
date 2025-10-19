```json
{
  "id": "91190351a1c8bd62",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292622,
  "host_pid": "9e6742732c60:1",
  "hash": "1d624cfa700d7795746ddcc6c879b637591763999c39f5ecb9bd8fed5adc42e8",
  "cid": "QmV11d624cfa700d7795746ddcc6c879b63759176399",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292622,
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
      "evaluated_at": 1760292622
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
  "sig": "0112d276f1356837ddf268dbe023fe748a97738c077bc64120191b503280aeba"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 357223800655087
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 34182663, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285765, 'matching_hash': '6810f1ba8ee75217'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '357223803', 'validation_error': 'Invalid routing number checksum'}}}