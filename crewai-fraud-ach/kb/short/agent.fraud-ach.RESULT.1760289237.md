```json
{
  "id": "6bac461ba8bda9f5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289237,
  "host_pid": "9e6742732c60:1",
  "hash": "87524cc5f4710840d7ac414996b5688ad789f70d2ba46a417bb65e2583d45856",
  "cid": "QmV187524cc5f4710840d7ac414996b5688ad789f70d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289237,
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
      "evaluated_at": 1760289237
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
  "sig": "2fd0f71aaca9213aeb07a2f2326f49ccee2f2b804723a4810944148a592f3944"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598206386
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 36335403, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285765, 'matching_hash': '83614fe1c845b0af'}}}