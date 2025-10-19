```json
{
  "id": "e8cccd1fba2bdcc7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294481,
  "host_pid": "9e6742732c60:1",
  "hash": "01080e5b2d6121873ef86bd49207a05c968b25843487132c636a4ab17ff1b85a",
  "cid": "QmV101080e5b2d6121873ef86bd49207a05c968b2584",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294481,
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
      "evaluated_at": 1760294481
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
  "sig": "ff26dfd50fa80496879bd9420ecf856459fc7230a790c6fa5b4c3b297bc50cb5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158500131
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 15666689, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': 'd40f962f80a48e01'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '530764331', 'validation_error': 'Invalid routing number checksum'}}}