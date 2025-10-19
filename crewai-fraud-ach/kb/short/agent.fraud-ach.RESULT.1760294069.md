```json
{
  "id": "9b0dbd64572a32f9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294069,
  "host_pid": "9e6742732c60:1",
  "hash": "64bf28fae209cdd6f297ab2dd3eaaadac270a47852411150c33bd2f106c2582c",
  "cid": "QmV164bf28fae209cdd6f297ab2dd3eaaadac270a478",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294069,
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
      "evaluated_at": 1760294070
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
  "sig": "d72caf803b93203051a4763366897127970c926810009b32101deab301cc3d5e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037758614
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 18927216, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': '8cf13377232eef82'}}}