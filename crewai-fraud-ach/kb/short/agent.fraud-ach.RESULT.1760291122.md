```json
{
  "id": "d2f02422c75a9680",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291122,
  "host_pid": "9e6742732c60:1",
  "hash": "4a5ca6b9ae4c465295af83640e03a56149dc29f389dca64b0cfcde1148602c06",
  "cid": "QmV14a5ca6b9ae4c465295af83640e03a56149dc29f3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291122,
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
      "evaluated_at": 1760291122
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
  "sig": "bb6be0fe1d6bfc1f1e0594a677eaef6b89169c9353b32b38b4c537995cfb0fb3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035430994
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 70941600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285765, 'matching_hash': '24f97a880bb92d0e'}}}