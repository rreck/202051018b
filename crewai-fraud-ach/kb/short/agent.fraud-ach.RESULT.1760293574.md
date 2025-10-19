```json
{
  "id": "2dae8ba49fb73575",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293574,
  "host_pid": "9e6742732c60:1",
  "hash": "1730d307b91d8530f9a1f014b9180b83f7238559a2cc8457617c9dbec9cfeff9",
  "cid": "QmV11730d307b91d8530f9a1f014b9180b83f7238559",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293574,
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
      "evaluated_at": 1760293574
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
  "sig": "d3e9c79cd995290fdead9361e05a42a6657b2bf95d4cb2fe6b768d71dc1ef94b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278613406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 91055094, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285765, 'matching_hash': 'bc206509fe1a9621'}}}