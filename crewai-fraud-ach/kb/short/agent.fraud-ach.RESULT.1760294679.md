```json
{
  "id": "da4daddf8915f33a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294679,
  "host_pid": "9e6742732c60:1",
  "hash": "025554bd6000ea342dd76625bdafeffd2f847850a05d130d1fcb0bdc3c1012dc",
  "cid": "QmV1025554bd6000ea342dd76625bdafeffd2f847850",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294679,
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
      "evaluated_at": 1760294679
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
  "sig": "e5a85f5ccc60177acbfe3f2e6c0d97d19f6de34bb961179d54a60bc218370315"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467961793
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 16215694, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285765, 'matching_hash': '7ef856857e97207f'}}}