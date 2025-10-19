```json
{
  "id": "7445aa0b928ccd6e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287501,
  "host_pid": "9e6742732c60:1",
  "hash": "22ec39cdad0a2080defcbf0b1bdd843d8aa87d56ebf12cf30d3adc9c2b274a4e",
  "cid": "QmV122ec39cdad0a2080defcbf0b1bdd843d8aa87d56",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287501,
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
      "evaluated_at": 1760287501
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
  "sig": "09550db68ddf26c0b3efeebc1a166a034ecfa5b53a9745f6d1b5a8d19f576be1"
}
```

Fraud detected: invalid_routing (score: 84)
Transaction: 272809904666410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50, 'total_amount': 19278032, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760285765, 'matching_hash': 'b8be43189937b834'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '272809901', 'validation_error': 'Invalid routing number checksum'}}}