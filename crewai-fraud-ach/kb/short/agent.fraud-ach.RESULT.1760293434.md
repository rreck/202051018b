```json
{
  "id": "a22bebb70a972397",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293434,
  "host_pid": "9e6742732c60:1",
  "hash": "9be8d2255212bb133ccc151492ab906577b2a325c3d2225c1359cb9759d33eaa",
  "cid": "QmV19be8d2255212bb133ccc151492ab906577b2a325",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293434,
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
      "evaluated_at": 1760293434
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
  "sig": "c381236657bf40c52d234742fba2a65ef32ca0f6aca052b978caa68ebe14b2c5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248125638
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 96691502, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285764, 'matching_hash': '28ad2138639324d3'}}}