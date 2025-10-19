```json
{
  "id": "c4b61a547793f245",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286344,
  "host_pid": "9e6742732c60:1",
  "hash": "03108c04ad1716d13451265fd7612de6106e17d5b1c47f62424d75048cca99a0",
  "cid": "QmV103108c04ad1716d13451265fd7612de6106e17d5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286344,
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
      "evaluated_at": 1760286344
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
  "sig": "073d12a85df3d129a12a192e2d399b35e054304778ed588e6465b73ace21d927"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000020807792
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285764, 'matching_hash': '8390351bce6e669b'}}}