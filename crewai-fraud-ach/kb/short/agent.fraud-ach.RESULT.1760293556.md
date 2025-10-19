```json
{
  "id": "21abbe909f45fad4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293556,
  "host_pid": "9e6742732c60:1",
  "hash": "d4f6eeccd1381e2aa510e0e5dc898194849e9c4fc082e11d76cc044f1d4c976f",
  "cid": "QmV1d4f6eeccd1381e2aa510e0e5dc898194849e9c4f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293556,
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
      "evaluated_at": 1760293556
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
  "sig": "4ecb51ac1e80fc919523ee70ce63cb02cc04f3e6ae07d48eb2cfed6e7ab5b84a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028779608
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 66515696, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': 'f4a7019387fd02e9'}}}