```json
{
  "id": "4f3418ed86bcd5df",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290325,
  "host_pid": "9e6742732c60:1",
  "hash": "7cc2c7d19c16201c1f84450c120d817dfb88490e1818cdd6642277faa0d10b02",
  "cid": "QmV17cc2c7d19c16201c1f84450c120d817dfb88490e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290325,
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
      "evaluated_at": 1760290325
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
  "sig": "37261083f2b099b9663456893929014d32178aeb0eac7f8f1bc5bb7e77ad4a38"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 130120308000996
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 36049398, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285765, 'matching_hash': 'd5206edc25c84cce'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '130120307', 'validation_error': 'Invalid routing number checksum'}}}