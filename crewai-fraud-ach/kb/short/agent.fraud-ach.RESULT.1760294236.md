```json
{
  "id": "ab2116560ba38ccd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294236,
  "host_pid": "9e6742732c60:1",
  "hash": "39ee492e068e2a94ae4f4e820a232679ca281ed7c4827fe21f7374eebab38b65",
  "cid": "QmV139ee492e068e2a94ae4f4e820a232679ca281ed7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294236,
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
      "evaluated_at": 1760294236
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
  "sig": "d803ed4c3f45695e5a6e697501618c6439a4e0a929fa50266159e555f6146bce"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 053611743401753
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 47679840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285764, 'matching_hash': 'ed032d3a1e3d03a7'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '053611749', 'validation_error': 'Invalid routing number checksum'}}}