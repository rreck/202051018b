```json
{
  "id": "bcb7b84b83ff2b79",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293702,
  "host_pid": "9e6742732c60:1",
  "hash": "dd7853df852bb2df8f3df65b8e1f94f031ac5e5bdbc53d665d7a1d8f03e42c3f",
  "cid": "QmV1dd7853df852bb2df8f3df65b8e1f94f031ac5e5b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293702,
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
      "evaluated_at": 1760293702
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
  "sig": "c31d11b9137634f4720aab342af27081318ae258c438e7cf1cc0830aae3cda89"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591752071
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 24517248, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': 'afb8628b94bcbefe'}}}