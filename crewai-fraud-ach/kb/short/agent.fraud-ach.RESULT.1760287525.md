```json
{
  "id": "ade8ed49f9b7c40b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287525,
  "host_pid": "9e6742732c60:1",
  "hash": "f77ea5e5d4d4561940585ef493779cfbc60765d4f06a2494cf32f525331f4b8e",
  "cid": "QmV1f77ea5e5d4d4561940585ef493779cfbc60765d4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287525,
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
      "evaluated_at": 1760287525
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
  "sig": "7cae425e7eee17ecbeaf17b46c77d2daaece39c42ee66f70da0ee2a7af65d240"
}
```

Fraud detected: invalid_routing (score: 85)
Transaction: 378944435908589
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50, 'total_amount': 14776461, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285763, 'matching_hash': '7919df3bb7d07869'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '378944430', 'validation_error': 'Invalid routing number checksum'}}}