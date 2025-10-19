```json
{
  "id": "80ac4cb33ee465aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285820,
  "host_pid": "9e6742732c60:1",
  "hash": "e6494d3040c75c8ba510866cb86796c92335945af1e5892deb1f3d81cb7230cd",
  "cid": "QmV1e6494d3040c75c8ba510866cb86796c92335945a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285820,
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
      "evaluated_at": 1760285820
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
  "sig": "72ee081e373b5e889d057c2350ac67887a5d15c89c615f6711b92dfc8f4dac7c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026691588
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 3, 'first_seen': 1760285763, 'matching_hash': '1da0382cf03ec7d2'}}}