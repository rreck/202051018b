```json
{
  "id": "5446b7b74d94da1c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287762,
  "host_pid": "9e6742732c60:1",
  "hash": "9888d998360ec17340b633a7390c4f74d339905d3c18ae24c8edaa2e4a8af5a4",
  "cid": "QmV19888d998360ec17340b633a7390c4f74d339905d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287762,
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
      "evaluated_at": 1760287762
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "c75765d0560fe2f57a2558352f88ec8c8bea1184b3e551d9cd5824408ddd5d6c"
}
```

Fraud detected: round_amount_pattern (score: 72)
Transaction: 111000026431469
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50, 'total_amount': 71000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285765, 'matching_hash': '51112ae34069fd52'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}