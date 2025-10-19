```json
{
  "id": "67a661c11f38de03",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288588,
  "host_pid": "9e6742732c60:1",
  "hash": "240537dee6ba6af418f60c766792384625974cab934539afd3477fffe58fc59e",
  "cid": "QmV1240537dee6ba6af418f60c766792384625974cab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288588,
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
      "evaluated_at": 1760288588
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
  "sig": "2e80e665543152a392ccfa83a52be6393e5cc2f0129853c093704aec593e200c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038503048
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50, 'total_amount': 33791478, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285763, 'matching_hash': '8e1259c289f167a8'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '041887155', 'validation_error': 'Invalid routing number checksum'}}}