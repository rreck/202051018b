```json
{
  "id": "f09088a8a90bc48d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291061,
  "host_pid": "9e6742732c60:1",
  "hash": "e1f9bb7f2ac02df3cf31c86e3627b01cc100d3dc08db2a4a67a29d800c8a8bae",
  "cid": "QmV1e1f9bb7f2ac02df3cf31c86e3627b01cc100d3dc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291061,
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
      "evaluated_at": 1760291061
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
  "sig": "c7474ece96588ab78a4ed7ec269f993d807219d605fe690c56f91caaacc86d71"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469045536
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 56912934, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285763, 'matching_hash': 'd92613c41315e1ec'}}}