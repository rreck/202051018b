```json
{
  "id": "de62a3ba1b7f4dec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293477,
  "host_pid": "9e6742732c60:1",
  "hash": "ab4fa9b5b37b1fd0528e88d54c6a13208d11b58c57b8554a630a6de8fca7a5f7",
  "cid": "QmV1ab4fa9b5b37b1fd0528e88d54c6a13208d11b58c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293477,
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
      "evaluated_at": 1760293477
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
  "sig": "c004127961bab24fdcd2fc8be2dc43370bacee288037d66428a6a59580eb0b14"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155104424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 63000168, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285763, 'matching_hash': 'b81635ada84cf521'}}}nd_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}