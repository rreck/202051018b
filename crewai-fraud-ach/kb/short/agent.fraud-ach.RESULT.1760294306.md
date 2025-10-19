```json
{
  "id": "7bdb773b468279bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294306,
  "host_pid": "9e6742732c60:1",
  "hash": "fc1322d95bf415578b2df5aa01e2751e01b844937f3d1a5b6d6b5becb7855fb2",
  "cid": "QmV1fc1322d95bf415578b2df5aa01e2751e01b84493",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294306,
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
      "evaluated_at": 1760294306
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
  "sig": "e082fb83de61d913381c55f294d9ccb9f5789f6a9fdca7680c931240ed0db6d8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274571178
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 111849895, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285765, 'matching_hash': '2fe0a786c074c752'}}}