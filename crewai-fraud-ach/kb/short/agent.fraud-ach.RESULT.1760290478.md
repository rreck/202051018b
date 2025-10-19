```json
{
  "id": "6bb5f0d3ddfbd4a4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290478,
  "host_pid": "9e6742732c60:1",
  "hash": "d82291cf5658cf4eb7fc944ccf18178060bb06d60dd3f9c7c2a2cf138f873778",
  "cid": "QmV1d82291cf5658cf4eb7fc944ccf18178060bb06d6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290478,
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
      "evaluated_at": 1760290478
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
  "sig": "f6ea76aca0181eababb89b35887fa226374d2351cf9649a264033a369267158e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596502557
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 16405244, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285764, 'matching_hash': 'c368684e8d9c7f24'}}}