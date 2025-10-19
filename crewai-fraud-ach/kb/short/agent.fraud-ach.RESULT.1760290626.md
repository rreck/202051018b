```json
{
  "id": "21446eef59f2cc01",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290626,
  "host_pid": "9e6742732c60:1",
  "hash": "da29aa1e882b53d553f4879a3a090c125821031f925cfd4139451b3a01071d06",
  "cid": "QmV1da29aa1e882b53d553f4879a3a090c125821031f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290626,
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
      "evaluated_at": 1760290626
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
  "sig": "9a11c4436370fcbb6426419dab7c818c2ac2bf2263c336b92dbc9923a670deae"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032200831
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285764, 'matching_hash': 'cae8555d53751756'}}}