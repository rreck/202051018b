```json
{
  "id": "ce99d5f050754c08",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294669,
  "host_pid": "9e6742732c60:1",
  "hash": "8afd4138116d350840ab312b9c8588c0243750a8504c1a1fcf47b8f1a8f4da78",
  "cid": "QmV18afd4138116d350840ab312b9c8588c0243750a8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294669,
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
      "evaluated_at": 1760294669
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
  "sig": "05971860004b6aadfcc24a6d818becfe7ef4d60e8fc83927f61a20812336e9c3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027165618
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 63257106, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': '01e7bf5fcf2bbeec'}}}