```json
{
  "id": "23b15f3f22aa2ee4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291395,
  "host_pid": "9e6742732c60:1",
  "hash": "e379d7f998763ac18c643c378fb88e39f456278c3dcd5cfe2767015c0e7d7625",
  "cid": "QmV1e379d7f998763ac18c643c378fb88e39f456278c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291395,
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
      "evaluated_at": 1760291395
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
  "sig": "24fbcc159352c04df7d0374e73ee341c773c407f645b20990fee148a9a511b47"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026797438
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 64939410, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285764, 'matching_hash': '15a6693010fc8a85'}}}