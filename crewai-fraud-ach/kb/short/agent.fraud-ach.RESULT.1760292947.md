```json
{
  "id": "8f237ae67a389de8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292947,
  "host_pid": "9e6742732c60:1",
  "hash": "39135f012b2cf97feef0282afc6790a2fddc221d3c4fa5710e611da3a87e0c1e",
  "cid": "QmV139135f012b2cf97feef0282afc6790a2fddc221d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292947,
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
      "evaluated_at": 1760292947
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
  "sig": "55c0e93a5b78760b2f6a43a419e13d0975c4418268e25f7d7ded97f1342f7fd8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468284841
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 38959024, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285764, 'matching_hash': 'af26bab6e9f38d2a'}}}