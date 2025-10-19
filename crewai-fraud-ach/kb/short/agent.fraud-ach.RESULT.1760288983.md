```json
{
  "id": "7666018d41d804a6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288983,
  "host_pid": "9e6742732c60:1",
  "hash": "e6d42a270a1a545c4674f806277553cc82a778d1424fcfa511ca390ebdc90a43",
  "cid": "QmV1e6d42a270a1a545c4674f806277553cc82a778d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288983,
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
      "evaluated_at": 1760288984
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
  "sig": "f4e5c0e55545cfa5ec9504b7cab72f1e4f5edda736d5f5c766d10fca6f605aee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248193290
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50, 'total_amount': 21799360, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285763, 'matching_hash': '8925647bbeca80db'}}}