```json
{
  "id": "92059d5ee738e1fd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294643,
  "host_pid": "9e6742732c60:1",
  "hash": "1efbaa10703780ff2f7b045f0a999dced902e4f448a6a9aa9a5e1d2730b30932",
  "cid": "QmV11efbaa10703780ff2f7b045f0a999dced902e4f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294643,
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
      "evaluated_at": 1760294643
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
  "sig": "6a272e62acfb5ec9ba6dba73794c4daaee7bc81633d387482f9f4b82c854f1bd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246611704
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 71993548, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': '524463c0aee194a0'}}}