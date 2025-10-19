```json
{
  "id": "4b3fa31008a2b878",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294771,
  "host_pid": "9e6742732c60:1",
  "hash": "6e629e6bf0f395edf524675705ce15d700d90305583f03aed5f759c42351c363",
  "cid": "QmV16e629e6bf0f395edf524675705ce15d700d90305",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294771,
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
      "evaluated_at": 1760294771
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
  "sig": "8210f82b7c540b0f675e34d74d0c3743ef2dc3975949b28e74a695b0bde68a54"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036272460
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 82461020, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': '9a32e66a4f8079bf'}}}