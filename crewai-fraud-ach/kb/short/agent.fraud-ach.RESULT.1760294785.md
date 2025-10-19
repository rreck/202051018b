```json
{
  "id": "83802c53a0cee0aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294785,
  "host_pid": "9e6742732c60:1",
  "hash": "e154e50dae1b6b53d878559b58e78dc8d4eecf7a9fd05413567cc3047fa58c5d",
  "cid": "QmV1e154e50dae1b6b53d878559b58e78dc8d4eecf7a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294785,
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
      "evaluated_at": 1760294785
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
  "sig": "506e75a739a45e0ff35f9c7adec9c54d82274792d21cd562c876ea7a4d9fdb07"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025001245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 52106932, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285764, 'matching_hash': 'bf601f225a65579b'}}}