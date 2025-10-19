```json
{
  "id": "5376935e866b2d75",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289251,
  "host_pid": "9e6742732c60:1",
  "hash": "a016c48ff2d10fde3b16ca27dcf333e54950bdb67d8775e16e3bbf84db43c83f",
  "cid": "QmV1a016c48ff2d10fde3b16ca27dcf333e54950bdb6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289251,
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
      "evaluated_at": 1760289251
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
  "sig": "1fbc3d08dfcb41da5ca016a87ce7ae7779ab0b6005ed1d00474817c0af7f7f46"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035823466
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 51525880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285763, 'matching_hash': 'b8896a43cee69b83'}}}