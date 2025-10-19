```json
{
  "id": "74013fb10bea71be",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292059,
  "host_pid": "9e6742732c60:1",
  "hash": "28265a0bf98896835d762f0c11734d331569ad09d3d131da87f2c3a05872702a",
  "cid": "QmV128265a0bf98896835d762f0c11734d331569ad09",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292059,
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
      "evaluated_at": 1760292059
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
  "sig": "68472f9d7b22cd054300b726d15d535f5fff4caab5dc6a7f0ecba1c950249d74"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 818309298369568
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 89039790, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285765, 'matching_hash': '9e3984c977816ea5'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '818309298', 'validation_error': 'Invalid routing number checksum'}}}