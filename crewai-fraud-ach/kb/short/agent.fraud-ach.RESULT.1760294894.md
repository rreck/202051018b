```json
{
  "id": "1f05c27ecbd5193b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294894,
  "host_pid": "9e6742732c60:1",
  "hash": "647c3aa3e57c43e1defa7f369d2d345c6cf3bf636534e5edbba7ab41e9717233",
  "cid": "QmV1647c3aa3e57c43e1defa7f369d2d345c6cf3bf63",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294894,
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
      "evaluated_at": 1760294894
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
  "sig": "e026240279f2e980935fb90a778676e88f0461c0299bd55cd692e35c2b9b1818"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469526930
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 27989388, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285764, 'matching_hash': 'b6b808f7611ea662'}}}